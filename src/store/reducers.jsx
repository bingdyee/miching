import { combineReducers } from 'redux-immutable';
import ChartsReducer from '../charts/reducer';
import ComponentsReducer from '../components/reducer';
import ViewsReducer from '../views/reducer';


export default combineReducers({
    charts: ChartsReducer,
    views: ViewsReducer,
    components: ComponentsReducer
})