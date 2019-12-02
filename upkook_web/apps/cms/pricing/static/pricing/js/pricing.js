function featuresVisible() {
  var allFeatures = document.getElementById("product-all-features");
  var dropDownArrow = document.getElementById("dropdown-arrow");
  if (allFeatures.hidden === true) {
    allFeatures.hidden = false;
    dropDownArrow.innerHTML = "&#9650;"
  } else {
    allFeatures.hidden = true;
    dropDownArrow.innerHTML = "&#9660;"

  }
}

window.addEventListener("load", function () {
  document.getElementById("product-features-dropdown").addEventListener("click", featuresVisible);
});
