import { useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CssBaseline from "@mui/material/CssBaseline";
import Grid from "@mui/material/Grid";
import Container from "@mui/material/Container";
import GitHubIcon from "@mui/icons-material/GitHub";
import FacebookIcon from "@mui/icons-material/Facebook";
import XIcon from "@mui/icons-material/X";
import { createTheme, ThemeProvider } from "@mui/material/styles";
//import "./App.css";
import Home from "./pages/Home";
import Header from "./components/General/Header";
import Footer from "./components/General/Footer";

const sections = [
	{ title: "NFL", url: "#" },
	{ title: "NBA", url: "#" },
	{ title: "MLB", url: "#" },
	{ title: "NHL", url: "#" },
	{ title: "PGA", url: "#" },
	{ title: "MLS", url: "#" },
	{ title: "UFC", url: "#" },
	{ title: "WNBA", url: "#" },
];

const defaultTheme = createTheme({
	typography: {
		fontFamily: ["Georgia"].join(","),
	},
});

function App() {
	return (
		<>
			<Router>
				<ThemeProvider theme={defaultTheme}>
					<CssBaseline />
					<Container maxWidth="lg">
						<Header title="Sports Snippets" sections={sections} />
						<main>
							<Routes>
								<Route path="/" element={<Home />} />
							</Routes>
						</main>
					</Container>
					<Footer title="" description="" />
				</ThemeProvider>
			</Router>
		</>
	);
}

export default App;
