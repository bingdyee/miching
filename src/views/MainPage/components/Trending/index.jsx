import React from 'react';
import { withStyles, Typography } from '@material-ui/core';
import styles from './styles';

class Trending extends React.PureComponent {

    render() {
        const { classes } = this.props;
        return (
            <div className={classes.root}>
                <Typography variant="h6" className={classes.title}>大 盘 分 析</Typography>
                <div className={classes.content}>
                </div>
            </div>
        )
    }

}

export default withStyles(styles)(Trending);