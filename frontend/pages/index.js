import React from 'react';
import Link from "next/link";
import { Button } from "@/components/ui/button";
import { useRouter } from 'next/router' // Import useRouter

export default function Home() {

  const router = useRouter() // Use useRouter hook to get the router object

  // Function to handle navigation to the login page
  const navigateToLogin = () => {
    router.push('/login') // Replace '/login' with the path to your login page
  }
  const navigateToSignUp = () => {
    router.push('/signup') // Replace '/login' with the path to your login page
  }
  
  return (
    <div className="min-h-screen bg-black text-white">
      <header className="flex justify-between items-center p-4">
        <div className="flex items-center space-x-4">
          <img
            alt="Products"
            className="h-10 w-10"
            height="40"
            src="/placeholder.svg"
            style={{
              aspectRatio: "40/40",
              objectFit: "cover",
            }}
            width="40"
          />
          <h1 className="text-xl font-bold">AskVideo</h1>
        </div>
        <nav className="space-x-4">
          <Link className="text-blue-500 hover:text-blue-700" href="#">
            About
          </Link>
          <Link className="text-blue-500 hover:text-blue-700" href="#">
            Features
          </Link>
        </nav>
      </header>
      <main className="flex justify-between items-center px-4 py-20">
        <section className="max-w-md">
          <h2 className="text-4xl font-bold mb-6">
            Welcome to AskVideo.
          </h2>
          <p className="mb-8">Express your gratitude with a personalized message.</p>
          <div className="space-x-4">
            <Button className="bg-blue-500 hover:bg-blue-700 text-white" onClick={navigateToLogin}>Log in</Button>
            <Button className="bg-blue-500 hover:bg-blue-700 text-white" onClick={navigateToSignUp}>Sign up</Button>
          </div>
        </section>
        <section className="max-w-md" id="about">

        </section>
      </main>
      <footer className="flex justify-center items-center p-4">

      </footer>
    </div>
  )
}

