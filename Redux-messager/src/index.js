import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import firebase from 'firebase';
import { Provider } from 'react-redux';
import store from './store';


// Your web app's Firebase configuration
const firebaseConfig = {
apiKey: "AIzaSyAtGj0zcbZiZBbeaz-G254e0nsd9g-rm10",
  authDomain: "commerce-max-f5637.firebaseapp.com",
  projectId: "commerce-max-f5637",
  storageBucket: "commerce-max-f5637.appspot.com",
  messagingSenderId: "291031635060",
  appId: "1:291031635060:web:ceb7abe1edec5b9b85ed21"
};


firebase.initializeApp(firebaseConfig);



ReactDOM.render(
  <Provider store={store}>
    <React.StrictMode>
      <App />
    </React.StrictMode>
  </Provider>,
  document.getElementById('root')
);


serviceWorker.unregister();
