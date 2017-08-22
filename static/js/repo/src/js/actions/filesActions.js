import axios from "axios";

export function fetchFiles() {
  return function(dispatch) {
    dispatch({type: "FETCH_FILES"});


    axios.get(`/api/v1/files/${window.props.repo_id}`)
      .then((response) => {
        console.log('data.files', response.data)
        dispatch({type: "FETCH_FILES_FULFILLED", payload: response.data.files})
        dispatch({type: "FETCH_IS_AUTHOR_FULFILLED", payload: response.data.is_owner})
      })
      .catch((err) => {
        dispatch({type: "FETCH_FILES_REJECTED", payload: err})
      })
  }
}
