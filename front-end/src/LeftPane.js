import React, { Component } from 'react';

import Header from './Header';

import './LeftPane.css';


class LeftPane extends Component {
  render() {
    return (
      <div className="container" style={{backgroundColor: 'red', height: '100%'}}>
            <div className="row left-block" onClick={() => {this.props.changeRightPane("add-entry")}}>
                Add Entry
            </div>
            <div className="row left-block" onClick={() => {this.props.changeRightPane("view-entry")}}>
                View Entry
            </div>
            <div className="row left-block">
                More down the way
            </div>
      </div>
    );
  }
}

export default LeftPane;
