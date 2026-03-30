import { useState } from "react";

import AnalyzerForm from "../components/AnalyzerForm";
import ResultCard from "../components/ResultCard";
import { analyzeInput } from "../services/api";

function HomePage() {
  const [mode, setMode] = useState("link");
  const [inputValue, setInputValue] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!inputValue.trim()) {
      setError("Please enter a URL or message before analyzing.");
      setResult(null);
      return;
    }

    setIsLoading(true);
    setError("");

    try {
      const response = await analyzeInput(mode, inputValue.trim());
      setResult(response);
    } catch (requestError) {
      setResult(null);
      setError(requestError.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main className="min-h-screen px-6 py-12">
      <div className="mx-auto flex max-w-5xl flex-col gap-8">
        <header className="space-y-4">
          <span className="inline-flex rounded-full border border-green-500/30 bg-green-500/10 px-3 py-1 text-xs font-semibold uppercase tracking-[0.3em] text-green-300">
            CYBRIX AI
          </span>
          <div className="space-y-3">
            <h1 className="max-w-3xl text-4xl font-bold tracking-tight text-white sm:text-5xl">
              Cybersecurity analysis platform foundation
            </h1>
            <p className="max-w-2xl text-base text-slate-300 sm:text-lg">
              This starter UI connects to the FastAPI backend and shows placeholder results for
              link and message analysis.
            </p>
          </div>
        </header>

        <section className="grid gap-6 lg:grid-cols-[1.15fr_0.85fr]">
          <AnalyzerForm
            inputValue={inputValue}
            isLoading={isLoading}
            mode={mode}
            onInputChange={setInputValue}
            onModeChange={setMode}
            onSubmit={handleSubmit}
          />
          <ResultCard error={error} result={result} />
        </section>
      </div>
    </main>
  );
}

export default HomePage;
