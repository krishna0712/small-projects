let swiperCards = new Swiper('.card__content', {
  slidesPerView: 3,
  loop: true,
  spaceBetween: 30,
  grabCursor: true,
  pagination: {
    el: '.swiper-pagination',
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});

// Function to update slidesPerView based on screen width
const updateSlidesPerView = () => {
  const width = window.innerWidth;
  if (width < 480) {
    swiperCards.params.slidesPerView = 1;
  } else if (width < 768) {
    swiperCards.params.slidesPerView = 2;
  } else {
    swiperCards.params.slidesPerView = 3;
  }
  swiperCards.update();
};

// Initial check
updateSlidesPerView();

// Add event listener for screen resize
window.addEventListener('resize', updateSlidesPerView);