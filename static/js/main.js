// Initialize AOS
AOS.init({
    duration: 800,
    easing: "ease-out",
    once: true,
    offset: 100,
});

// Initialize GLightbox
const lightbox = GLightbox({
    selector: ".glightbox",
    touchNavigation: true,
    loop: true,
});

// Gallery filter
document.querySelectorAll(".gallery-filter .btn").forEach(function (btn) {
    btn.addEventListener("click", function () {
        document
            .querySelectorAll(".gallery-filter .btn")
            .forEach(function (b) {
                b.classList.remove("active");
            });
        this.classList.add("active");

        var filter = this.getAttribute("data-filter");
        document.querySelectorAll(".gallery-item").forEach(function (item) {
            if (filter === "all" || item.getAttribute("data-category") === filter) {
                item.style.display = "block";
            } else {
                item.style.display = "none";
            }
        });
    });
});
