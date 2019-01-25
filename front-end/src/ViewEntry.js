import React, { Component } from 'react';
import './AddEntry.css';


class ViewEntry extends Component {
  render() {
    return (
      <div className="container" style={{backgroundColor: 'lime', height: '100%', width: '100%'}}>

            <div className="row" style={{backgroundColor: 'purple', height: 50, padding: 10}}>
                Enter the details to view a Place
            </div>

            <form style={{paddingTop: 10}}>
                <div className="form-group" >
                    
                    <div className="row">
                        <div className="col-md-6">
                            <div className="row">
                                <div className="col-md-2">
                                    Name
                                </div>
                                <div className="col-md-9">
                                    <input type="text" className="form-control" id="place" placeholder="Enter Name"/>
                                </div>
                            </div>
                        </div>
                        <div className="col-md-6">
                            <div className="row">
                                <div className="col-md-2">
                                    Country
                                </div>
                                <div className="col-md-9">
                                    <input type="text" className="form-control" id="place" placeholder="Enter Country"/>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div className="form-group" >
                    
                    <div className="row">
                        <div className="col-md-6">
                            <div className="row">
                                <div className="col-md-2">
                                    State
                                </div>
                                <div className="col-md-9">
                                    <input type="text" className="form-control" id="place" placeholder="Enter State"/>
                                </div>
                            </div>
                        </div>
                        <div className="col-md-6">
                            <div className="row">
                                <div className="col-md-2">
                                    City
                                </div>
                                <div className="col-md-9">
                                    <input type="text" className="form-control" id="place" placeholder="Enter City"/>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <button type="submit" class="btn btn-primary">Submit</button>
            </form>

            <div className="row" style={{marginTop: 20, width: '100%', paddingRight: 0,marginLeft: '0.05%'}}>
                <div className="accordion" id="accordion" style={{width: '100%', paddingRight: 0}}>
                    <div className="card" style={{width: '100%', paddingRight: 0}}>
                        <div className="card-header" id="headingOne">
                            <h5 className="mb-0">
                                <button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne" >
                                    Item #1
                                </button>
                            </h5>
                        </div>

                        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
                        <div className="card-body">
                        <form style={{paddingTop: 10}}>
                            <div className="form-group" >
                                
                                <div className="row">
                                    <div className="col-md-6">
                                        <div className="row">
                                            <div className="col-md-2">
                                                Name
                                            </div>
                                            <div className="col-md-9">
                                                <input type="text" className="form-control" id="place" placeholder="Enter Name"/>
                                            </div>
                                        </div>
                                    </div>
                                    <div className="col-md-6">
                                        <div className="row">
                                            <div className="col-md-2" style={{PaddingRight: 0, paddingLeft: 0}}>
                                                Country
                                            </div>
                                            <div className="col-md-9">
                                                <input type="text" className="form-control" id="place" placeholder="Enter Country"/>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div className="form-group" >
                                
                                <div className="row">
                                    <div className="col-md-6">
                                        <div className="row">
                                            <div className="col-md-2">
                                                State
                                            </div>
                                            <div className="col-md-9">
                                                <input type="text" className="form-control" id="place" placeholder="Enter State"/>
                                            </div>
                                        </div>
                                    </div>
                                    <div className="col-md-6">
                                        <div className="row">
                                            <div className="col-md-2">
                                                City
                                            </div>
                                            <div className="col-md-9">
                                                <input type="text" className="form-control" id="place" placeholder="Enter City"/>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <button type="submit" class="btn btn-primary">Submit</button>
                        </form>

                        </div>
                        </div>
                    </div>
                </div>
            </div>
      </div>
    );
  }
}

export default ViewEntry;
