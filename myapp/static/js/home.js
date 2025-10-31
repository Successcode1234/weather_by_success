window.addEventListener('load', () => {
  const loader = document.querySelector('.loader_parent');
  const percentageText = document.querySelector('.percentage_done');
  const welcome = document.querySelector('.welcome');
  const parent_location_choosing = document.querySelector('.parent_location_choosing');

  // Loader percentage
  gsap.to({ val: 0 }, {
    val: 100,
    duration: 3,
    onUpdate: function() {
      percentageText.textContent = Math.round(this.targets()[0].val) + '%';
    },
    onComplete: function() {
      setTimeout(() => {
        gsap.to(loader, { duration: 1, opacity: 0, pointerEvents: 'none' });
        welcome.style.display = 'flex'; // ensure welcome is visible
        animateWelcome(); // show welcome after loader
      }, 1000);
    }
  });

  // Animate welcome screen
  function animateWelcome() {
    const icon = document.querySelector('.welcome_icon');
    const heading = document.querySelector('.wlc_text h2');
    const paragraphs = document.querySelectorAll('.wlc_text p');
    const button = document.querySelector('.continue_btn');

    // Set initial positions for animation
    gsap.set([heading, paragraphs, button], { y: 20, opacity: 0 });

    const tl = gsap.timeline({ defaults: { ease: "power2.out" } });

    tl.from(icon, { duration: 1, scale: 0, opacity: 0, y: -50 })
      .to(heading, { duration: 0.8, opacity: 1, y: 0 }, "-=0.5");

    paragraphs.forEach((p, i) => {
      tl.to(p, { duration: 0.6, opacity: 1, y: 0 }, "-=0.4");
    });

    tl.to(button, { duration: 0.6, opacity: 1, y: 0 }, "-=0.3");
  }

  // Continue button
  document.querySelector('.continue_btn').addEventListener("click", () => {
  gsap.to(welcome, {
    duration: 0.8,
    opacity: 0,
    y: -50,
    pointerEvents: 'none',
    onComplete: closeWelcome
  });
});

  // Request location
//   function requestLocation() {
//     if (navigator.geolocation) {
//       navigator.geolocation.getCurrentPosition(
//         pos => console.log("User coords:", pos.coords),
//         err => alert("Location access denied or unavailable.")
//       );
//     } else {
//       alert("Geolocation is not supported by your browser.");
//     }
//   }


function closeWelcome() {
  // Make the location container visible before animation
  parent_location_choosing.style.visibility = 'visible';
  parent_location_choosing.style.display = 'flex';

  welcome.style.display = 'none'; // hide welcome immediately after button click

  // Animate location container in
  gsap.fromTo(parent_location_choosing, 
    { opacity: 0 }, 
    { duration: 0.8, opacity: 1, pointerEvents: 'auto' }
  );

}


});