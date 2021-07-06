export default (state = {}, action) => {

    switch (action.type) {

        case 'ERROR':
            return {
                ...state,
                error: action.error
            };

        case 'MOUNT_ERROR_POPUP':
            return {
                ...state,
                errorPopupIsMount: true
            };

        case 'UNMOUNT_ERROR_POPUP':
            return {
                ...state,
                errorPopupIsMount: false
            };

        case 'INFO':
            return {
                ...state,
                info: action.info
            };

        default:
            return state;
    }

};
