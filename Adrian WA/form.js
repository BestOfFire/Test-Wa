const form = document.getElementById("form");
form.addEventListener("submit", (e) => {
    e.preventDefault();
    const name = document.getElementById("name").value;
    const rank = document.getElementById("rank").value;
    const youtube = document.getElementById("youtube").value;

    const xhr = new XMLHttpRequest();
    xhr.open("GET", "data.py?name=" + name + "&rank=" + rank + "&youtube=" + youtube);
    xhr.send();

    xhr.onload = () => {
        if (xhr.status === 200) {
            alert("Data has been saved successfully.");
        } else {
            alert("An error has occurred.");
        }
    }
});