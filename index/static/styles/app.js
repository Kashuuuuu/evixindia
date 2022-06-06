//Get the button
let mybutton = document.getElementById("btn-back-to-top");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  // TOP TO BOTTOM BUTTON
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }

  // CHANGE NAVBAR
  let navbar = document.querySelector(".navbar");
  let dealerBtn = document.querySelector("#become-dealer-btn");
  let navLinks = document.querySelectorAll(".nav-link");
  if (window.scrollY > 620) {
    // NABAR
    navbar.classList.remove("bg-light");
    navbar.classList.add("bg-dark");

    // DEALER-BUTTON
    dealerBtn.classList.remove("btn-dark");
    dealerBtn.classList.add("btn-outline-light");

    // NAV-LINK
    navLinks.forEach((navLink) => {
      navLink.classList.remove("text-dark");
      navLink.classList.add("text-light");
    });
  } else {
    // NAVBAR
    navbar.classList.remove("bg-dark");
    navbar.classList.add("btn-outline-light");

    // DEALER-BUTTON
    dealerBtn.classList.remove("btn-outlind-light");
    dealerBtn.classList.add("btn-dark");

    // NAV-LINK
    navLinks.forEach((navLink) => {
      navLink.classList.remove("text-light");
      navLink.classList.add("text-dark");
    });
  }
}
// When the user clicks on the button, scroll to the top of the document
mybutton.addEventListener("click", backToTop);

function backToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

// PRODUCT SWIPER
var swiper = new Swiper(".mySwiper", {
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});
// PRODUCT SWIPER

// HIGHLIGHTS

var mySwiper = new Swiper(".swiper-container", {
  speed: 400,
  spaceBetween: 100,
  initialSlide: 0,
  //truewrapper adoptsheight of active slide
  autoHeight: false,
  // Optional parameters
  direction: "horizontal",
  loop: true,
  // delay between transitions in ms
  autoplay: 5000,
  autoplayStopOnLast: true, // loop false also
  // If we need pagination
  pagination: ".swiper-pagination",
  paginationType: "bullets",

  // Navigation arrows
  nextButton: ".swiper-button-next",
  prevButton: ".swiper-button-prev",

  // And if we need scrollbar
  //scrollbar: '.swiper-scrollbar',
  // "slide", "fade", "cube", "coverflow" or "flip"
  effect: "slide",
  // Distance between slides in px.
  spaceBetween: 10,
  //
  slidesPerView: 4,
  //
  centeredSlides: true,
  //
  slidesOffsetBefore: 0,
  //
  grabCursor: true,
});

// TESTIMONIAL
$(".team-slider").owlCarousel({
  loop: true,
  nav: false,
  autoplay: true,
  autoplayTimeout: 5000,
  smartSpeed: 450,
  margin: 20,
  responsive: {
    0: {
      items: 1,
    },
    768: {
      items: 2,
    },
    991: {
      items: 3,
    },
    1080: {
      items: 4,
    },
    1920: {
      items: 4,
    },
  },
});

//First Carousel
$(".first-carousel").owlCarousel({
  items: 1,
  loop: true,
  nav: false,
  autoplay: true,
  autoplayTimeout: 5000,
  smartSpeed: 450,
  margin: 0,
});
