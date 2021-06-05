import { describe, it, expect } from "@jest/globals";
import { MyLambdaClient } from "aws-sdk";

const LambdaClient = new MyLambdaClient();

describe("lambda fcn client-config-svc", () => {
  it("GET can respond", async () => {
    //Arrange
    const data = new TextEncoder("UTF-8").encode(
      JSON.stringify({
        path: "/client-config-svc/",
        httpMethod: "GET",
      })
    );
    //Act
    const response = await LambdaClient.invoke({
      FunctionName: "client-config-svc",
      payload: data,
    });
    //Assert
    expect(response.statusCode).toBe(200);
    expect(response.body).toBe();
  });
});
