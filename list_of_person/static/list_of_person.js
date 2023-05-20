 const options = document.querySelectorAll('.sort-option .option');
  const selectedOption = "{% if sort_option %}{{ sort_option }}{% endif %}";

  options.forEach(option => {
    if (option.getAttribute('data-value') === selectedOption) {
      option.classList.add('selected');
    }

    option.addEventListener('click', () => {
      options.forEach(o => o.classList.remove('selected'));
      option.classList.add('selected');

      const value = option.getAttribute('data-value');
      console.log('Выбрано значение:', value);
    });
  });