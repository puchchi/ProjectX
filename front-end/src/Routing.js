import React, {Component} from 'react';
import {Route, withRouter} from 'react-router-dom';

import Home from './Home';

class Routing extends Component {
  constructor(props) {
    super(props);

    this.state={
        view: 'add-entry'
    }

  }

  changeRightPane = (view) => {
        this.setState({
            view: view
        });
  };

    render() {
        return (
            <div style={{height: '100%'}}>

                <Route exact path="/" render={() => (
                    <div style={{height: '100%'}}>
                        <Home changeRightPane={this.changeRightPane} currentView={this.state.view}/>
                    </div>
                )}/>
            </div>
        );
    }
}

export default withRouter(Routing);
