import React, { useEffect, useState } from "react";
import axiosInstance from '../axios';

// Material-UI

import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Link from '@material-ui/core/Link';
import CssBaseline from '@material-ui/core/CssBaseline';
import Paper from '@material-ui/core/Paper';
import CardMedia from '@material-ui/core/CardMedia';

// Theme

import theme from './theme';
import { CardContent, Grid, ThemeProvider, Typography } from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
    paper: {
        marginTop: theme.spacing(8),
        alignItems: 'center',
		color: "#e2b714",
    },
    cardMedia: {
        paddingTop: '56.25%',
    },
    link: {
        margin: theme.spacing(1, 1.5),
        color: "#e2b714",
    },
    cardHeader: {
        backgroundColor: "primary",
    },
    postTitle: {
        fontSize: '20px',
        textAlign: 'left',
        color: "#e2b714",
    },
    postText: {
        display: 'flex',
        justifyContent: 'left',
		alignItems: 'baseline',
		fontSize: '10px',
		textAlign: 'left',
		marginBottom: theme.spacing(1),
        color: "#e2b714",
    },
}));

const Posts = (props) => {
    const { posts } = props;
    const classes = useStyles();
    if (!posts || posts.length === 0) return <p>Cannot find any posts! Sorry</p>;
    return (
        <React.Fragment>
            <ThemeProvider theme = { theme } >
            <CssBaseline/>
            <Container maxWidth="md" component="main">
                <div className={ classes.paper }>
                    <Grid container spacing={5} alignItems="flex-end">
                        {posts.map((post) =>{
                            return (
                                <Grid item key = { post.id } xs={ 12 } md={ 4 }>
                                    <Link color="secondary" href={ "/" } className={ classes.link }>
                                        <CardMedia className={ classes.cardMedia } image={ post.media } title="Image title" />
                                    </Link>
                                    <CardContent className={ classes.cardContent }>
                                        <Typography gutterBottom variant="h4" component="h2" color="secondary" className={ classes.postTitle }>{ post.title.substr(0, 50) }...</Typography>
                                        <div className={ classes.postText }>
                                            <Typography color="secondary">{ post.content.substr(0, 40) }</Typography>
                                        </div>
                                    </CardContent>
                                </Grid>
                            );
                        })}
                    </Grid>
                    </div>
            </Container>
            </ThemeProvider>
        </React.Fragment>
    );
};

function PostLoadingComponent(Component) {
	return function PostLoadingComponent({ isLoading, ...props }) {
		if (!isLoading) return <Component {...props} />;
		return (
            <ThemeProvider theme = { theme }>
            <CssBaseline />
			<p style={{ fontSize: '25px' }}>
				We are waiting for the data to load!...
			</p>
            </ThemeProvider>
		);
	};
}

export default function Feed(){
    const PostLoading = PostLoadingComponent(Posts);
    const [appState, setAppState] = useState({
        loading: true,
        posts: null,
    });

    const classes = useStyles();

    useEffect(() =>{
        axiosInstance.get('/threads/').then((res) =>{
            const allPosts = res.data;
            console.log(res.data);
            setAppState({ loading: false, posts: allPosts });
            console.log(res.data);
        });
    }, [setAppState]);
    return (
        <ThemeProvider theme={ theme }>
        <CssBaseline />
        <div className="feed">
            <Paper elevation = { 12 } stype = { { padding: 4, backgroundColor: "primary", border: "1px" } }>
            <Typography component="h1" variant="h2" color="secondary" className={ classes.link }>Latest Posts</Typography>
            </Paper>
            <PostLoading isLoading={ appState.loading } posts={ appState.posts } />
        </div>
        </ThemeProvider>
    );
}