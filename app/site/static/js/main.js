const alerts = document.querySelector('#notification');

// Add is-active class to current selected menu
const currentLocation = location.href;
const menuItem = document.querySelectorAll('a');
const currentItem = document.querySelector('.is-active');
const length = menuItem.length;

for (let i = 0; i < length; i++) {
  if (menuItem[i].href === currentLocation) {
    currentItem.classList.remove('is-active');
    menuItem[i].classList.add('is-active');
  }
}

// Hide Alert Messages after 4 seconds
setTimeout(() => {
  if (alerts) {
    alerts.style.display = 'None';
  }
}, 4000);
