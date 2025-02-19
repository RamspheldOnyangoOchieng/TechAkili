document.addEventListener("DOMContentLoaded", function() {
    console.log("Initializing Swiper...");

    var swiper = new Swiper(".swiper-container", {
        loop: true, 
        slidesPerView: 4, 
        spaceBetween: 20, 
        autoplay: {
            delay: 2000,
            disableOnInteraction: false, 
        },
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
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



// Open & Close Popup Form
document.querySelector(".popup-form-container").classList.add("show");

document.querySelector(".close-btn").addEventListener("click", function() {
    document.querySelector(".popup-form-container").classList.remove("show");
});


