document.addEventListener('DOMContentLoaded', function () {
    const filterItems = document.querySelectorAll('.list');
    const productItems = document.querySelectorAll('.itemBox');

    // Show all images by default
    productItems.forEach(item => {
        item.style.display = 'block';
    });

    filterItems.forEach(item => {
        item.addEventListener('click', function () {
            const dataFilter = item.getAttribute('data-filter');

            if (dataFilter !== 'all') {
                filterItems.forEach(filter => {
                    filter.classList.remove('active');
                });
                item.classList.add('active');
            } else {
                item.classList.toggle('active');
                if (item.classList.contains('active')) {
                    filterItems.forEach(filter => {
                        filter.classList.remove('active');
                    });
                    item.classList.add('active');
                }
            }

            for (let j = 0; j < productItems.length; j++) {
                if (dataFilter !== 'all' && productItems[j].getAttribute('data-item') !== dataFilter) {
                    productItems[j].style.display = 'none';
                } else {
                    productItems[j].style.display = 'block';
                }
            }
        });
    });

    const goToTop = document.querySelector('.gototop');
    goToTop.addEventListener('click', function () {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});
