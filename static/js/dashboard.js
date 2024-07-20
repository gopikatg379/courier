document.addEventListener('DOMContentLoaded', function() {
    var collapsibleElements = document.querySelectorAll('[data-toggle="collapse"]');

    collapsibleElements.forEach(function(element) {
        element.addEventListener('click', function() {
            var consignor = this.getAttribute('href').substring(1); // Get target id without '#'
            var targetElement = document.getElementById(consignor);
            var arrow = this.querySelector('.arrow');

            if (targetElement.classList.contains('show')) {
                arrow.classList.remove('rotate');
            } else {
                arrow.classList.add('rotate');
            }
        });
    });
});
document.addEventListener('DOMContentLoaded', function() {
    var collapsibleElements = document.querySelectorAll('[data-toggle="collapse"]');

    collapsibleElements.forEach(function(element) {
        element.addEventListener('click', function() {
            var masterMenu = this.getAttribute('href').substring(1); // Get target id without '#'
            var targetElement = document.getElementById(masterMenu);
            var arrow = this.querySelector('.arrow');

            if (targetElement.classList.contains('show')) {
                arrow.classList.remove('rotate');
            } else {
                arrow.classList.add('rotate');
            }
        });
    });
});
document.addEventListener('DOMContentLoaded', function() {
    var collapsibleElements = document.querySelectorAll('[data-toggle="collapse"]');

    collapsibleElements.forEach(function(element) {
        element.addEventListener('click', function() {
            var consignee = this.getAttribute('href').substring(1); // Get target id without '#'
            var targetElement = document.getElementById(consignee);
            var arrow = this.querySelector('.arrow');

            if (targetElement.classList.contains('show')) {
                arrow.classList.remove('rotate');
            } else {
                arrow.classList.add('rotate');
            }
        });
    });
});
