import React from 'react';
import { Provider } from 'react-redux';
import store from './store';
import useStyles from './styles';

function App() {
  useStyles();
  return (
      <Provider store={store}>
        <div className="App">
          Hello ECharts
        </div>
      </Provider>
  );
}

export default App;
