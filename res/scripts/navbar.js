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
    console.log(cont.innerText);
  }

  //   console.log(window.location.href.split("/")[3]);
});

console.log();
// console.log(window.location.href.split("/")[3]);
