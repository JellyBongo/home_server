import {combineReducers, compose, createStore} from 'redux';
import {connectRouter} from 'connected-react-router';
import {reducer as formReducer} from 'redux-form';
import {createBrowserHistory} from 'history';

import errorReducer from './reducers/errorReducer';

const history = createBrowserHistory();
const initialState = {};

let composeEnhancers = compose;

const enhancers = [];

const reducers = {
    router: connectRouter(history),
    form: formReducer,
    errorStore: errorReducer,
};

const store = createStore(
    combineReducers(reducers),
    initialState,
    composeEnhancers(...enhancers)
);

export {store, history};
