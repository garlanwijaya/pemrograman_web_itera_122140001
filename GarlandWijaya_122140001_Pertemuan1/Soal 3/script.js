document.getElementById("myForm").addEventListener("submit", function (e) {
  e.preventDefault();

  // Validasi semua field
  const isNameValid = validateName();
  const isEmailValid = validateEmail();
  const isPasswordValid = validatePassword();

  if (isNameValid && isEmailValid && isPasswordValid) {
    alert("Form submitted successfully!");
    // Di sini bisa ditambahkan logika pengiriman form ke server
  }
});

async function validateInput(field) {
  switch (field) {
    case "name":
      await validateName();
      break;
    case "email":
      await validateEmail();
      break;
    case "password":
      await validatePassword();
      break;
  }
}

function validateName() {
  const name = document.getElementById("name").value.trim();
  const error = document.getElementById("nameError");

  console.log(`Name validation: ${name}`);

  if (name.length <= 3) {
    console.log("Name is invalid");
    error.textContent = "Nama harus lebih dari 3 karakter";
    error.classList.remove("hidden");
    return false;
  } else {
    console.log("Name is valid");
    error.textContent = "";
    error.classList.add("hidden");
    return true;
  }
}

function validateEmail() {
  const email = document.getElementById("email").value.trim();
  const error = document.getElementById("emailError");
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  console.log(`Email validation: ${email}`);

  if (!emailRegex.test(email)) {
    console.log("Email is invalid");
    error.textContent = "Email tidak valid";
    error.classList.remove("hidden");
    return false;
  } else {
    console.log("Email is valid");
    error.textContent = "";
    error.classList.add("hidden");
    return true;
  }
}

function validatePassword() {
  const password = document.getElementById("password").value;
  const error = document.getElementById("passwordError");

  console.log(`Password validation: ${password}`);

  if (password.length < 8) {
    console.log("Password is invalid");
    error.textContent = "Password minimal 8 karakter";
    error.classList.remove("hidden");
    return false;
  } else {
    console.log("Password is valid");
    error.textContent = "";
    error.classList.add("hidden");
    return true;
  }
}
