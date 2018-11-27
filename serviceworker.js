var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/static/core/css/estilos.css',
    '/static/core/Img/adoptados/Apolo.jpg',
    '/static/core/Img/adoptados/Duque.jpg',
    '/static/core/Img/adoptados/Tom.jpg',
    '/static/core/Img/rescatados/Bigotes.jpg',
    '/static/core/Img/rescatados/Chocolate.jpg',
    '/static/core/Img/rescatados/Luna.jpg',
    '/static/core/Img/rescatados/Maya.jpg',
    '/static/core/Img/rescatados/Oso.jpg',
    '/static/core/Img/rescatados/Pexel.jpg',
    '/static/core/Img/rescatados/Wifi.jpg',
    '/static/core/Img/crowfunding.jpg',
    '/static/core/Img/logo.png',
    '/static/core/Img/PatitaIcono.png',
    '/static/core/Img/perro.png',
    '/static/core/Img/rescate.jpg',
    '/static/core/Img/social-inst.png',
    '/static/core/Img/social-twitter.png',
    '/static/core/Img/socialfacebook.png',
    '/static/core/Img/socialplus.png',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.css',
    'https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.min.js',
    '/static/core/js/inicializacion.js'
]

self.addEventListener('install',function(event){
    
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(function(cache) {
                console.log('Opened cache');
                return cache.addAll(urlsToCache);
            })
    );
});

self.addEventListener('fetch', function(event){
    event.respondWith(
        caches.match(event.request).then(function(response){
            if(response) {
                return response;
            }
            return fetch(event.request);
        })
    );
});

importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var config = {
    apiKey: "AIzaSyDSXdVUDpy1eIjMlBsXr8MoJcpbSxTy1gs",
    authDomain: "misperris-b93c6.firebaseapp.com",
    databaseURL: "https://misperris-b93c6.firebaseio.com",
    projectId: "misperris-b93c6",
    storageBucket: "misperris-b93c6.appspot.com",
    messagingSenderId: "510377586996"
  };
  firebase.initializeApp(config);

  const messaging = firebase.messaging();

 //programamos una funcion que estara escuchando cuando llegue una notificacion desde firebase

 messaging.setBackgroundMessageHandler(function(payload) {

    //el payload contendrá el mensaje destinado al usuario
    var title = "notificacion"
    var options = {
        body:"este es el cuerpo del mensaje"
    }

        //mostramos la notificacion al usuario
        return self.registration.showNotification(title, options);

    })