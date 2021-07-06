import axios from "./axios";

const apiPrefix = '/api/';

export const showError = (dispatch, errorMessage) => {
    dispatch({type: "MOUNT_ERROR_POPUP"});
    dispatch({
        type: `ERROR`,
        error: errorMessage && errorMessage !== '' ? errorMessage : 'Произошла неизвестная ошибка'
    })
};

export const hideError = (dispatch) => {

    setTimeout(() => {
        dispatch({type: "UNMOUNT_ERROR_POPUP"})
    }, 0);

    dispatch({
        type: `ERROR`,
        error: null
    })
};