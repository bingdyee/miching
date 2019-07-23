import { combineReducers } from 'redux-immutable';
import ComponentsReducer from '../components/reducer';
import ViewsReducer from '../views/reducer';


export default combineReducers({
    views: ViewsReducer,
    components: ComponentsReducer
})