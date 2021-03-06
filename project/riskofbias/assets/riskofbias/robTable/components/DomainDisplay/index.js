import React, { Component } from 'react';
import PropTypes from 'prop-types';
import _ from 'lodash';

import MetricDisplay from 'riskofbias/robTable/components/MetricDisplay';
import MetricForm from 'riskofbias/robTable/components/MetricForm';

class DomainDisplay extends Component {
    render() {
        let { domain, config, updateNotesLeft } = this.props;
        return (
            <div>
                <h3>{domain.key}</h3>
                {_.map(domain.values, (metric) => {
                    let props = {
                        key: metric.key,
                        ref: _.last(metric.values).id,
                        metric,
                        config,
                    };
                    return config.isForm ? (
                        <MetricForm {...props} updateNotesLeft={updateNotesLeft} />
                    ) : (
                        <MetricDisplay {...props} />
                    );
                })}
                <hr />
            </div>
        );
    }
}

DomainDisplay.propTypes = {
    domain: PropTypes.shape({
        key: PropTypes.string.isRequired,
        values: PropTypes.array.isRequired,
    }).isRequired,
    config: PropTypes.object,
    updateNotesLeft: PropTypes.func,
};

export default DomainDisplay;
