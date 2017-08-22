export default function reducer(state={
    files: {},
    fetching: false,
    fetched: false,
    error: null,
    is_owner: null
  }, action) {

    switch (action.type) {
      case "FETCH_FILES": {
        return {...state, fetching: true}
      }
      case "FETCH_FILES_REJECTED": {
        return {...state, fetching: false, error: action.payload}
      }
      case "FETCH_FILES_FULFILLED": {
        return {
          ...state,
          fetching: false,
          fetched: true,
          files: action.payload,
        }
      }
      case "FETCH_IS_AUTHOR_FULFILLED": {
        return {
          ...state,
          is_owner: action.payload
        }
      }
      // case "ADD_TWEET": {
      //   return {
      //     ...state,
      //     repos: [...state.repos, action.payload],
      //   }
      // }
      // case "UPDATE_TWEET": {
      //   const { id, text } = action.payload
      //   const newTweets = [...state.repos]
      //   const tweetToUpdate = newTweets.findIndex(tweet => tweet.id === id)
      //   newTweets[tweetToUpdate] = action.payload;
      //
      //   return {
      //     ...state,
      //     repos: newTweets,
      //   }
      // }
      // case "DELETE_TWEET": {
      //   return {
      //     ...state,
      //     repos: state.repos.filter(tweet => tweet.id !== action.payload),
      //   }
      // }
    }

    return state
}
