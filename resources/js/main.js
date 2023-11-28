const login_button = document.getElementById("Login")


login_button.addEventListener('click', getData)

async function getData() {
    await fetch("http://127.0.0.1:5000/register", {
    method: "POST",
    body: JSON.stringify({
        username: "balls",
        Password: "balls"
    }),
    headers: {
        "Content-type": "application/json; charset=UTF-8",
        "Access-Control-Allow-Origin": "*"

    }
    })
    .then((response) => response.json())
    .then((json) => console.log(json));
}