import "./App.css";
import { render } from "react-dom";
import { useForm } from "react-cool-form";

const Field = ({ label, id, error, ...rest }) => (
  <div>
    <div>
      <label htmlFor={id}>{label}</label>
    </div>
    <input id={id} {...rest} />
    {error && <p>{error}</p>}
  </div>
);

function App() {
  const { form, use } = useForm({
    defaultValues: { email: "", coin: "", difference_percentage: "" },
    onSubmit: (values) => alert(JSON.stringify(values, undefined, 2))
  });
  const errors = use("errors", { errorWithTouched: true });

  return (
    <form ref={form} noValidate>
      <Field
        label="Email"
        id="email"
        name="email"
        type="email"
        required
        error={errors.email}
      />
      <Field
        label="Coin"
        id="coin"
        name="coin"
        type="string"
        // Support built-in validation
        required
        error={errors.coin}
      />
      <Field
        label="Difference Percentage"
        id="difference_percentage"
        name="difference_percentage"
        type="integer"
        required
        minLength={8}
        error={errors.password}
      />
      <input type="submit" />
    </form>
  );
}

render(<App />, document.getElementById("root"));


export default App;
