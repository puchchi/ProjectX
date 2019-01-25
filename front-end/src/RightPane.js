import React, { Component } from 'react';

import AddEntry from './AddEntry';
import ViewEntry from './ViewEntry';

class RightPane extends Component {

    componentWillMount() {
        console.log("hello from RightPane");
        console.log(this.props.currentView);
    }


  render() {
    if(this.props.currentView === 'view-entry') {
        return (
        <div className="container" style={{backgroundColor: 'gray', height: '100%'}}>
            <ViewEntry />
        </div>
        );
    }
    else {
        return (
            <div className="container" style={{backgroundColor: 'gray', height: '100%'}}>
                <AddEntry />
            </div>
        );
    }

  }
}

export default RightPane;
