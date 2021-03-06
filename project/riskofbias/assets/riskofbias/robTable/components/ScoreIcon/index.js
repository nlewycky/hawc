import React, { Component } from 'react';
import PropTypes from 'prop-types';

import './ScoreIcon.css';

class ScoreIcon extends Component {
    render() {
        let { shade, symbol } = this.props;
        return (
            <div className="score-icon" style={{ backgroundColor: shade }}>
                {symbol}
            </div>
        );
    }
}

ScoreIcon.propTypes = {
    shade: PropTypes.string.isRequired,
    symbol: PropTypes.string.isRequired,
};

export default ScoreIcon;
