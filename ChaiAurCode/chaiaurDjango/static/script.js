// script.js

// Example 1: Smooth Scrolling for internal links (if you have them)
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Example 2: Simple Scroll Reveal (a more robust solution would use Intersection Observer or a library)
const sections = document.querySelectorAll('section');

const revealSection = (entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('fade-in');
            observer.unobserve(entry.target); // Stop observing once revealed
        }
    });
};

const sectionObserver = new IntersectionObserver(revealSection, {
    root: null, // viewport
    threshold: 0.15, // 15% of the section must be visible
});

sections.forEach(section => {
    section.classList.add('hidden-section'); // Add initial hidden class in CSS
    sectionObserver.observe(section);
});

// Add this to your style.css for the scroll reveal
/*
.hidden-section {
    opacity: 0;
    transform: translateY(20px);
    transition: opacity 0.6s ease-out, transform 0.6s ease-out;
}

.fade-in {
    opacity: 1;
    transform: translateY(0);
}
*/