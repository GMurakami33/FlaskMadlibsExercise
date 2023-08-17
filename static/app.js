document.addEventListener("DOMContentLoaded", function() {
  const form = document.querySelector("#submit");
  if (form) {
      form.addEventListener("submit", function(event) {
          const fields = form.querySelectorAll("input[type='text']");
          let isValid = true;

          fields.forEach(field => {
              if (field.value.trim().length < 3) {
                  isValid = false;
                  field.classList.add("invalid");
              } else {
                  field.classList.remove("invalid");
              }
          });

          if (!isValid) {
              event.preventDefault(); // Prevent form submission
              alert("All fields must be at least 3 characters long.");
          }
      });
  }
});