var carTOId = 0;

function handleChangeSlide(event) {
  var slideId = event.currentTarget.getAttribute('data-slide');
  changeSlide(slideId);
  clearTimeout(carTOId);
}

function getSlides() {
  return document.querySelectorAll(".car-slide");
}

window.addEventListener("load", function () {
  nextSlide(1);
  document.querySelectorAll(".slide-caption").forEach(function (caption) {
    caption.addEventListener('click', handleChangeSlide);
  });
  document.querySelectorAll(".slide-dot").forEach(function (dot) {
    dot.addEventListener('click', handleChangeSlide);
  });
});


// Next/previous controls
function nextSlide(index) {
  var slides = getSlides();
  if (index > slides.length) {
    index = 1;
  } else if (index < 1) {
    index = slides.length;
  }
  changeSlide("product-slide-" + index);

  carTOId = setTimeout(function () {
      nextSlide(index + 1);
    },
    7000
  );
}

function hideSlide(slide) {
  slide.classList.remove('car-slide-active');
  document.getElementById(slide.id + '-caption').classList.remove('slide-caption-active');
  document.getElementById(slide.id + '-dot').classList.remove('slide-dot-zoom');
}

function showSlide(slide) {
  slide.classList.add('car-slide-active');
  document.getElementById(slide.id + '-caption').classList.add('slide-caption-active');
  document.getElementById(slide.id + '-dot').classList.add('slide-dot-zoom');
}

function changeSlide(slideId) {
  getSlides().forEach(hideSlide);
  showSlide(document.getElementById(slideId));
}
