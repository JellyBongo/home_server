import axios from 'axios';
import {ConcurrencyManager} from 'axios-concurrency';
import {store} from "../configureStore";

const axiosInstance = axios.create({
    baseURL: window.config.apiUrl
});

axiosInstance.interceptors.response.use(
    (response) => {

        if (response.data && response.data.status && response.data.status.code !== 'OK') {
            store.dispatch({
                type: 'AJAX_ERROR',
                error: response.data.status.message
            });
            return Promise.reject(response.data.status.message);
        }

        if (response.config.method !== 'get') {
            store.dispatch({
                type: 'AJAX_INFO',
                info: response.data.message
            })
        }

        return Promise.resolve(response);
    },
    (error) => {

        if (error.response && error.response.status === 401) {
            setTimeout(() => window.location.reload(), 2000);
            throw new Error("Данные для авторизации запроса просрочены либо невалидны. Страница будет перезагружена.");
        }

        return Promise.reject(error);
    }
);

ConcurrencyManager(axiosInstance, 1);

export default axiosInstance;
