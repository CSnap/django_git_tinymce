import React from "react"
import axios from "axios";
import { connect } from "react-redux"

import { fetchRepo } from "../actions/repoActions"
import { fetchFiles } from "../actions/filesActions"
//import { fetchTags } from "../actions/tagsActions"


@connect((store) => {
  return {
    repo: store.repo.repo,
    files: store.files,
  };
})
export default class Layout extends React.Component {
  componentWillMount() {
    //this.props.dispatch(fetchUser())
    this.props.dispatch(fetchRepo())
    //this.props.dispatch(fetchTags())
    this.props.dispatch(fetchFiles())
  }

  getIcon(type) {
    switch(type) {
      case 'blob':
        return <i class="glyphicon glyphicon-list-alt"/>
      case 'tree':
        return <i class="glyphicon glyphicon-folder-close"/>
    }
  }




  render() {
    const { repo, files, is_author } = this.props;

    // if (!repos.length) {
    //   return <button onClick={this.fetchRepos.bind(this)}>load repos</button>
    // }

    //const mappedTweets = tweets.map(tweet => <li key={tweet.id}>{tweet.text}</li>)

    // const mappedRepos = this.props.repos.map(repo => {
    //   return  <a href={`/${repo.owner_username}/${repo.name}`.toLowerCase()} key={repo.id}><div className="col-md-4" ><img src="https://dummyimage.com/400x300/000/fff" width="100%" className="img-responsive"/>{repo.name} by { repo.owner_username }</div></a>
    // })
    //
    // const mappedTags = this.props.tags.map(tag => {
    //   function toTitleCase(str)
    //   {
    //       return str.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
    //   }
    //   let titled = toTitleCase(tag.title)
    //   console.log('titled', titled)
    //   return <li key={tag.id}><a href="#" >{titled}</a></li>
    // })
    console.log('this.props.files', this.props.files)
    console.log('files', files)
    console.log('this.props.files.fetched',this.props.files.fetched)

    // const filesTable = this.props.files.map((file) => {
    //   const icon = getIcon(file.type)
    //   const editLink = (is_author) ? <a href={`blob/${file.name}/edit`}>edit</a> : null
    //   return <li>{icon} <a href={`blob/${file.name}`}>{ file.name }</a> - <a href={`commit/${file.id}`}>{file.id}</a> - {editLink}</li>
    // })

    if (!this.props.files.fetched) {
            return <p>Loading…</p>;
        }
    return <div>
      <div className="row">
        <div className="col-md-12">
          <h1 className="text-center">Repo</h1>
        </div>
      </div>
      <div className="row">
        <div className="col-md-12">

          {this.props.files.files.map((file) => {
            const icon = this.getIcon(file.type)
            const editLink = (files.is_owner) ? <a href={`blob/${file.name}/edit`}>edit</a> : null
            return <li key={file.id}>{icon} <a href={`blob/${file.name}`}>{ file.name }</a> - <a href={`commit/${file.id}`}>{file.id}</a> {editLink}</li>
          })}


        </div>
      </div>

    </div>
  }
}
