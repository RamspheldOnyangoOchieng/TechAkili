function openForm() {
    document.getElementById("popup-form").style.display = "flex";
}

function closeForm() {
    document.getElementById("popup-form").style.display = "none";
}

document.addEventListener("DOMContentLoaded", function () {
    let index = 0;
    const groups = document.querySelectorAll(".partner-group");
    const totalGroups = groups.length;
    
    function showNextPartners() {
        index = (index + 1) % totalGroups;
        document.querySelector(".partner-slider").style.transform = `translateX(-${index * 100}%)`;
    }

    setInterval(showNextPartners, 3000); // Change every 3 seconds
});
