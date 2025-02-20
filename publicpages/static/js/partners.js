document.addEventListener("DOMContentLoaded", function() {
    console.log("Initializing Swiper...");

    var swiper = new Swiper(".swiper-container", {
        loop: true,
        slidesPerView: 4,
        spaceBetween: 20,
        autoplay: {
            delay: 2500,
            disableOnInteraction: false
        },
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev"
        },
        pagination: {
            el: ".swiper-pagination",
            clickable: true
        },
        breakpoints: {
            1024: { slidesPerView: 4 },
            768: { slidesPerView: 3 },
            480: { slidesPerView: 2 },
            320: { slidesPerView: 1 }
        }
    });

    console.log("Swiper Initialized:", swiper);
});

// Popup Form Functionality
function openForm() {
    document.getElementById("popup-form").style.display = "flex";
}

function closeForm() {
    document.getElementById("popup-form").style.display = "none";
}
