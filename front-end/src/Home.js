import React, { Component } from 'react';

import Header from './Header';
import LeftPane from './LeftPane';
import RightPane from './RightPane';

import './Home.css';

class Home extends Component {

    constructor(props) {
        super(props);
    
        this.state={
            
        }
    
    }

  render() {
    return (
        <div className="container-fluid" style={{height: '100%', width: '100%', paddingLeft: 0, paddingRight: 0}}>
            <Header />
            <div className="row" style={{height: '100%', width: '100%', paddingLeft: 0, paddingRight: 0}}>
                <div className="col-md-3" style={{height: '100%', paddingLeft: 0, paddingRight: 0}}>
                    <LeftPane changeRightPane={this.props.changeRightPane}/>
                </div>
                <div className="col-md-9" style={{height: '100%', paddingLeft: 0, paddingRight: 0}}>
                    <RightPane currentView={this.props.currentView} />
                </div>
            </div>
        </div>
    );
  }
}

export default Home;
