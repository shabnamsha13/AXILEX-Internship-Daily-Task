function validateRegister() {
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;

    if(name === "" || email === "" || password === "") {
        document.getElementById("msg").innerText = "All fields required!";
        return false;
    }

    alert("✅ You have successfully joined the Ramadan Wellness Planner!");
    document.getElementById("msg").innerText = "Registration Successful!";
    return false;
}

function validateLogin() {
    let email = document.getElementById("loginEmail").value;
    let password = document.getElementById("loginPassword").value;

    if(email === "" || password === "") {
        document.getElementById("loginMsg").innerText = "Enter email and password!";
        return false;
    }

    alert("🌙 Welcome back! Continue your Ramadan routine.");
    document.getElementById("loginMsg").innerText = "Login Successful!";
    return false;
}

function submitContact() {
    let name = document.getElementById("cname").value;
    let msg = document.getElementById("cmessage").value;

    if(name === "" || msg === "") {
        document.getElementById("contactMsg").innerText = "Fill all fields!";
        return false;
    }

    alert("🤲 Your Ramadan goal has been shared. Stay consistent!");
    document.getElementById("contactMsg").innerText = "Message Sent!";
    return false;
}