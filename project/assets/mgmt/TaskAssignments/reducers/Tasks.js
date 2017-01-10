import * as types from 'mgmt/TaskAssignments/constants';


const defaultState = {
    isFetching: false,
    isLoaded: false,
    list: [],
};

function tasks(state=defaultState, action) {
    switch (action.type) {
    case types.REQUEST_TASKS:
        return Object.assign({}, state, {
            isFetching: true,
            isLoaded: false,
        });

    case types.RECEIVE_TASKS:
        return Object.assign({}, state, {
            isFetching: false,
            isLoaded: true,
            list: action.tasks,
        });

    default:
        return state;
    }
}

export default tasks;
