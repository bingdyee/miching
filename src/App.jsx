import React from 'react';
import { Provider } from 'react-redux';
import { HashRouter, Route, Switch } from 'react-router-dom';
import store from './store';
import useStyles from './styles';
import * as pages from './views';


function App() {
  useStyles();
  return (
      <Provider store={store}>
        <HashRouter>
            <Switch>
                <Route exact path='/' component={pages.MainPage}/>
            </Switch>
        </HashRouter>
      </Provider>
  );
}

export default App;
