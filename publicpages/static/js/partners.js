// Function to open the popup form
function openForm() {
    document.getElementById("popup-overlay").style.display = "block";
    document.getElementById("popup-form").style.display = "block";
}

// Function to close the popup form
function closeForm() {
    document.getElementById("popup-overlay").style.display = "none";
    document.getElementById("popup-form").style.display = "none";
}

function openForm() {
    document.getElementById("popup-overlay").classList.add("active");
    document.getElementById("popup-form").classList.add("active");
}

function closeForm() {
    document.getElementById("popup-overlay").classList.remove("active");
    document.getElementById("popup-form").classList.remove("active");
}

// Open the popup form
function openForm() {
    document.getElementById("popup-overlay").classList.add("active");
    document.getElementById("popup-form").classList.add("active");
}

