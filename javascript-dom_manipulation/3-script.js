const toggle_header = document.querySelector('#toggle_header');
toggle_header.addEventListener('click', function() {
  const header = document.querySelector('header');
  if (header.classList.contains('green')) {
    header.classList = 'red';
  } else {
    header.classList = 'red';
  };
});
