let navbar = document.querySelector(".navbar");
let navbarul = navbar.querySelector("ul");
let navbarelem = navbarul.querySelectorAll("li");

navbarelem.forEach((el) => {
  let cont = el.querySelector("a");
  if (
    window.location.href.split("/")[3].toLowerCase() ===
    cont.innerText.toLowerCase()
  ) {
    el.classList.add("active");
  }

  //   console.log(window.location.href.split("/")[3]);
});

let menu_bar = document.querySelector(".menu-bar");
menu_bar.addEventListener("click", () => {
  if (navbarul.dataset.active === "true") {
    delete navbarul.dataset.active;
  } else {
    navbarul.dataset.active = "true";
  }
});
// console.log(window.location.href.split("/")[3]);
