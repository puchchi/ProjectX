import React, { Component } from 'react';
import './AddEntry.css';


class AddEntry extends Component {
  render() {
    return (
      <div className="container" style={{backgroundColor: 'lime', height: '100%'}}>
            <form action="#">
                <div className="form-group" style={{paddingTop: 10}}>
                    <div className="row">
                        <div className="col-md-8">
                            <input type="text" className="form-control" id="place" placeholder="Enter a place to search"/>
                        </div>
                        <div className="col-md-3">
                            <button className="btn btn-primary">Search</button>
                        </div>
                    </div>
                </div>
            </form>
            <form style={{paddingTop: 35}}>
                <div className="form-group" >
                    
                    <div className="row">
                        <div className="col-md-6">
                            <div className="row">
                                <div className="col-md-2">
                                    Latitude
                                </div>
                                <div className="col-md-9">
                                    <input type="text" className="form-control" id="place" placeholder="Latitude"/>
                                </div>
                            </div>
                        </div>
                        <div className="col-md-6">
                            <div className="row">
                                <div className="col-md-2">
                                    Longitude
                                </div>
                                <div className="col-md-9">
                                    <input type="text" className="form-control" id="place" placeholder="Longitude"/>
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
                                    <input type="text" className="form-control" id="place" placeholder="State"/>
                                </div>
                            </div>
                        </div>
                        <div className="col-md-6">
                            <div className="row">
                                <div className="col-md-2">
                                    Country
                                </div>
                                <div className="col-md-9">
                                    <input type="text" className="form-control" id="place" placeholder="Country"/>
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
                                    Address
                                </div>
                                <div className="col-md-9">
                                    <input type="text" className="form-control" id="place" placeholder="Address"/>
                                </div>
                            </div>
                        </div>
                        <div className="col-md-6">
                            <div className="row">
                                <div className="col-md-2">
                                    About
                                </div>
                                <div className="col-md-9">
                                    <textarea className="form-control" id="place" placeholder="About the place"/>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div className="form-group" >
                    
                    <div className="row">
                        <div className="col-md-1" style={{paddingRight: 0}}>
                            Map Url
                        </div>

                        <div className="col-md-9">
                            <input type="text" className="form-control" id="place" placeholder="Map url"/>
                        </div>
                                
                    </div>
                </div>

                <button type="submit" className="btn btn-primary">Submit</button>
            </form>
      </div>
    );
  }
}

export default AddEntry;
