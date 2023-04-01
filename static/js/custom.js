// Get Current Year
function getCurrentYear() {
    var d = new Date();
    var year = d.getFullYear();
    document.querySelector("#displayDateYear").innerText = year;
}
getCurrentYear()

//client section owl carousel
$(".owl-carousel").owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    dots: false,
    navText: [
        '<i class="fa fa-long-arrow-left" aria-hidden="true"></i>',
        '<i class="fa fa-long-arrow-right" aria-hidden="true"></i>'
    ],
    autoplay: true,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1
        },
        768: {
            items: 2
        },
        1000: {
            items: 2
        }
    }
});

/** google_map js **/

function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}

var navbarToggler = document.querySelector('.navbar-toggler');

navbarToggler.addEventListener('click', function() {
  navbarToggler.classList.toggle('active');
});



function formatPhone(event) {
  const phoneInput = event.target;
  let phoneNumber = phoneInput.value.replace(/[^\d]/g, '');

  // Удаляем префикс "+7("
  if (phoneNumber.startsWith('7')) {
    phoneNumber = phoneNumber.slice(1);
  }

  // Ограничиваем длину номера телефона
  phoneNumber = phoneNumber.slice(0, 10);

  let formattedPhoneNumber = '';

  if (phoneNumber.length > 0) {
    formattedPhoneNumber = '+7(';

    if (phoneNumber[0] === '8') {
      if (phoneNumber.length > 1) {
        formattedPhoneNumber += phoneNumber.slice(1, 4);
        phoneNumber = phoneNumber.slice(4);
      }
      if (phoneNumber.length > 2) {
        formattedPhoneNumber += ') ' + phoneNumber.slice(0, 3);
        phoneNumber = phoneNumber.slice(3);
      }
      if (phoneNumber.length > 1) {
        formattedPhoneNumber += phoneNumber[0] + '-' + phoneNumber.slice(1);
      } else {
        formattedPhoneNumber += phoneNumber;
      }
    } else {
      if (phoneNumber.length > 3) {
        formattedPhoneNumber += phoneNumber.slice(0, 3);
        phoneNumber = phoneNumber.slice(3);
      }
      if (phoneNumber.length > 3) {
        formattedPhoneNumber += ') ' + phoneNumber.slice(0, 3);
        phoneNumber = phoneNumber.slice(3);
      }
      if (phoneNumber.length > 2) {
        formattedPhoneNumber += '-' + phoneNumber.slice(0, 2);
        phoneNumber = phoneNumber.slice(2);
      }
      if (phoneNumber.length > 0) {
        formattedPhoneNumber += '-' + phoneNumber;
      }
    }

    // Удаляем тире после открывающей скобки
    if (formattedPhoneNumber.startsWith('+7(-')) {
      formattedPhoneNumber = '+7(' + formattedPhoneNumber.slice(4);
    }

    phoneInput.value = formattedPhoneNumber;
  } else {
    phoneInput.value = '';
  }
}